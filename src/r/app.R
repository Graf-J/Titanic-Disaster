library(shiny)
library(shinyjs)
library(readr)
library(parsnip)
library(workflows)
library(recipes)

options(shiny.host = "0.0.0.0")
options(shiny.port = 3001)

ui <- fluidPage(
  useShinyjs(),
  titlePanel("Titanic Survival Classifier 🚢"),

  sidebarLayout(
    sidebarPanel(
      fileInput("train_file", "Upload your train.csv", accept = ".csv"),

      # Hide test upload initially
      hidden(
        fileInput("test_file", "Upload your test.csv", accept = ".csv")
      ),

      # Hide download button initially
      hidden(
        downloadButton("download_preds", "💾 Download Predictions")
      )
    ),

    mainPanel(
      verbatimTextOutput("train_status"),
      tableOutput("pred_table")
    )
  )
)

server <- function(input, output, session) {

  # Reactive: Read Train Data
  train_data <- reactive({
    req(input$train_file)
    df <- read_csv(input$train_file$datapath)

    required_cols <- c(
      "PassengerId","Survived","Pclass","Name","Sex","Age",
      "SibSp","Parch","Ticket","Fare","Cabin","Embarked"
    )
    if(!all(required_cols %in% colnames(df))) {
      stop("Uploaded training file does not match expected structure.")
    }

    df$Survived <- as.factor(df$Survived)

    # Show test file upload now
    shinyjs::show("test_file")

    df
  })

  # Fit model
  model_fit <- reactive({
    req(train_data())

    rec <- recipe(Survived ~ ., data = train_data()) %>%
      step_rm(PassengerId, Name, Ticket, Cabin) %>%
      step_impute_mean(Age) %>%
      step_impute_mode(Embarked) %>%
      step_mutate(across(c(Pclass, Sex, Embarked), as.factor)) %>%
      step_dummy(c(Pclass, Sex, Embarked)) %>%
      step_normalize(all_of(c("Age","Fare")))

    log_model <- logistic_reg() %>% set_engine("glm") %>% set_mode("classification")

    wf <- workflow() %>% add_model(log_model) %>% add_recipe(rec)
    fit(wf, data = train_data())
  })

  # Show training status
  output$train_status <- renderText({
    req(model_fit())
    "✅ Model trained successfully!"
  })

  # Reactive: Read Test Data
  test_data <- reactive({
    req(input$test_file)
    df <- read_csv(input$test_file$datapath)

    required_cols <- c(
      "PassengerId","Pclass","Name","Sex","Age",
      "SibSp","Parch","Ticket","Fare","Cabin","Embarked"
    )
    if(!all(required_cols %in% colnames(df))) {
      stop("Uploaded test file does not match expected structure.")
    }

    # Show download button now
    shinyjs::show("download_preds")

    df
  })

  # Make predictions
  predictions <- reactive({
    req(model_fit(), test_data())

    pred <- predict(model_fit(), new_data = test_data())
    data.frame(
      PassengerId = test_data()$PassengerId,
      Survived = pred$.pred_class
    )
  })

  # Show first 10 predictions
  output$pred_table <- renderTable({
    head(predictions(), 10)
  })

  # Download predictions
  output$download_preds <- downloadHandler(
    filename = "predictions.csv",
    content = function(file) {
      write.csv(predictions(), file, row.names = FALSE)
    }
  )

}

shinyApp(ui, server)