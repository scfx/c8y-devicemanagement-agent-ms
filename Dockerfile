FROM debian:11-slim
ARG DEB_MIRROR=http://ftp.de.debian.org/debian
ENV DEBIAN_FRONTEND=noninteractive
ENV CONTAINER=docker
RUN echo "deb ${DEB_MIRROR} bullseye main" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
    python3 \
    python3-apt \
    python3-pip \    
	python3-websocket \
    python3-requests \
    openssh-server \    
    geoip-bin \
    geoip-database

RUN pip install c8ydm
RUN pip install flask
RUN mkdir /root/.cumulocity
COPY agent.ini /root/.cumulocity/agent.ini
COPY DM_Agent.json /root/.cumulocity/DM_Agent.json


CMD ["c8ydm.start"]