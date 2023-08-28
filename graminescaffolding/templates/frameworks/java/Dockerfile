{% extends 'Dockerfile' %}

{% block install %}
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends -y openjdk-17-jre-headless maven
{% endblock %}

{% block copy_app %}
COPY ./target /app
COPY ./.scag /app/.scag
{% endblock %}

{#- vim: set ft=jinja ts=4 sts=4 sw=4 et : #}
