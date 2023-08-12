import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='eduardolima',
    application_name='aws-python',
    app_uid='rJLvSqJJ1dbtgBPc1K',
    org_uid='2763e3ef-f172-4ee5-8198-690f45460aa4',
    deployment_uid='ec75671f-2434-455f-a8fb-96e5eda389e0',
    service_name='aws-python',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='6.2.3',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'aws-python-dev-delete_category', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('src/API/category/deleteCategory.delete')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
