FROM rocker/shiny:4.5.1

WORKDIR /app

COPY install_packages.R .

RUN Rscript install_packages.R

COPY . .

EXPOSE 3001

CMD ["Rscript", "app.R"]