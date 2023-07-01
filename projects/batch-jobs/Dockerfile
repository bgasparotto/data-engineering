FROM python:3.10-bookworm

# installs Poetry
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

# installs Java 8 for Spark
RUN mkdir -p /etc/apt/keyrings
RUN wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/keyrings/adoptium.asc
RUN echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list
RUN apt update
RUN apt install temurin-8-jre -y

# copies the project
COPY . app
WORKDIR app

# installs the project's modules including Spark
RUN poetry config virtualenvs.create false
RUN poetry install

# runs Spark with an empty script so it caches external required packages before use
ENV SPARK_EXTRA_PACKAGES "org.apache.hadoop:hadoop-aws:3.3.1,org.postgresql:postgresql:42.6.0"
RUN touch /tmp/empty.py
RUN spark-submit --packages=$SPARK_EXTRA_PACKAGES /tmp/empty.py
