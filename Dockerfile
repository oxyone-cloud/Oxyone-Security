FROM python:3.9-slim

WORKDIR /app

COPY index.html .
COPY anti_hack.py .

RUN touch security_alerts.log && chmod 666 security_alerts.log

RUN echo "#!/bin/sh\npython3 anti_hack.py &\npython3 -m http.server 8080" > /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8080

CMD ["/app/start.sh"]
