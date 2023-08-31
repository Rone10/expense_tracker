FROM nginx:1.25

# Remove default nginx website
RUN rm /etc/nginx/conf.d/default.conf
# Copy the nginx.conf file
COPY ./nginx.conf /etc/nginx/conf.d

# Expose port 80
# EXPOSE 80

# Run nginx
CMD ["nginx", "-g", "daemon off;"]

# Path: nginx/nginx.conf
# Compare this snippet from nginx.conf:
# events {
#     worker_connections  1024;
# }
#
# http {
#     server {
#         listen 80;
#         server_name localhost;
#         location / {
#             proxy_pass http://web:8000;
#             proxy_set_header Host $host;
#             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         }
#     }
# }
