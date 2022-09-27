# TheySay


Link: [TheySay.tech](https://theysay.tech) <br>

## About

As the project name suggests, TheySay analyzes data from social media, allowing you to find insight and ideas easier. <br>

This website is currently under construction. The functions currently online and are going to get online soon are:  <br>
- [x] Word Frequency (50%) <br>
- [ ] Geography visualization under a hashtag <br>
- [ ] Sentiment Change under a hashtag by time <br>

## Tech Part
#### Backend
- MongoDB
- Flask + uWSGI + Nginx 
- Oracle VMs
- spaCy.
#### Frontend
- React.js
- Vercel
### Pre-processing and Database
A problem with this project is how to process users' requests and give back a result as fast as possible in a small VM. <br>

For the "word frequency" scenario, users can input a keyword with the start and end times. If the server processes the raw data just when a request comes in, the time cost is about 30 secs on my m1 Macbook Pro with a not-very-accurate model ("en_core_web_sm" from spaCy). <br>

However, it's better to give the best accurate result to users by a more precise model, "en_core_web_trf," which takes more than 10 minutes of processing time.   <br>

Therefore,  a system that does the most time-consuming tasks and stores the result in the database with an acceptable minimal time granularity before the query are developed. The query waiting time is reduced from about 30 secs to an average of 0.02 sec.



