
#Kmart_Tech_challenge


The Solution uses the following tools
- Travis for CI and CD

## BUILD

 - Make is used to build the application that fetches the commit sha from the travis Environment variable and the version and the description from a metadata file in the app  

## Deployment
 - Create an S3 Bucket in an AWS account to store the cloudformation templates generated by AWS SAM
 - replace the bucket name in the `.travis.yml` file
  From the root of the folder run the following
```
sed -i e 's/niro-source/<new_bucket_name>/g .travis.yml'
```
 - Update the AWS credentials in the `env: ` codeblock in `.travis.yml`
 - Enable Travis in github apps 


## Risks and Limitations

- Credentials are stored in the repo ( they are encrypted however they are still in the repo), Mitigation would be to use instance profiles on the build environments
- AWS SAM is limited in its capabilites to extend the functionalities if needed ( I.E if further infrastructure was needed to be deployed then SAM has its limiations)
