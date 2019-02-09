<!--
title: 'AWS Serverless REST API with DynamoDB store example in Python'
description: 'This example demonstrates how to setup a RESTful Web Service allowing you to create, list, get, update and delete folders. DynamoDB is used to store the data.'
-->
# Serverless REST API

This example demonstrates how to setup a [RESTful Web Services](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) allowing you to create, list, get, update and delete folders. DynamoDB is used to store the data. This is just an example and of course you could use any data storage as a backend.

## Structure

This service has a separate directory for all the folder operations. For each operation exactly one file exists e.g. `folders/delete.py`. In each of these files there is exactly one function defined.

The idea behind the `folders` directory is that in case you want to create a service containing multiple resources e.g. users, notes, comments you could do so in the same service. While this is certainly possible you might consider creating a separate service for each resource. It depends on the use-case and your preference.

## Use-cases

- API for a Web Application
- API for a Mobile Application

## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

The expected result should provide:

```bash
endpoints:
  POST - https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders
  GET - https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders
  GET - https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/{id}
  PUT - https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/{id}
  DELETE - https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/{id}
```

To deploy a specific function:
```bash
serverless deploy function -f {function}
```

## Usage

You can create, retrieve, update, or delete folders with the following commands:

### Create a folder

```bash
curl -X POST https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folder --data '{ "name": "React Folder" }'
```

No output

### List all folders

```bash
curl https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders
```

### Get one folder

```bash
curl https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/<id>
```

### Update a folder

```bash
curl -X PUT https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/<id> --data '{ "name": "Serverless Folder"}'
```

### Delete a folder

```bash
curl -X DELETE https://ABCD1234.execute-api.us-east-1.amazonaws.com/dev/folders/<id>
```

## Scaling

### AWS Lambda

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

When you create a table, you specify how much provisioned throughput capacity you want to reserve for reads and writes. DynamoDB will reserve the necessary resources to meet your throughput needs while ensuring consistent, low-latency performance. You can change the provisioned throughput and increasing or decreasing capacity as needed.

This is can be done via settings in the `serverless.yml`.

```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```

In case you expect a lot of traffic fluctuation we recommend to checkout this guide on how to auto scale DynamoDB [https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/](https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/)
