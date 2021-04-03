# Project-Discord-Integration


## User Instruction


Enter an anime name to get its quotes. 
You can find all the names available here: https://animechan.vercel.app/api/available/anime  
To build the docker image, you can run `docker build -t discord .`  
To run the container you can enter: `docker run -e <discord token> discord -i naruto`

## Discord Integration Explanation
This project first take a parameter to retrieve remote data in a publicly-accessible API with anime information.
And then it will make a request to the API of Discord and the information will be posted to the channel in our Discord server. 



