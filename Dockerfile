FROM python:3-onbuild
EXPOSE 5000
CMD ["uvicorn", "restapi_app:app"]
