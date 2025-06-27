# TO DO

* [X] Extract the data in json format. Decide whether the data will remain in seperate tables or in an all-in-one file.
  * The new idea behind the model is that **it'll create a summary from the input data** (posts and comments from specific **subreddits**), and then it will display the stock prices of different companies or sectors. The model that will be using to summary the subreddit discussed topics, is the [LongT5](https://huggingface.co/google/long-t5-tglobal-base).
* [ ] Preprocessing the data (tokenization)
* [ ] Choose model
* [ ] Deploy model into AWS  EC2 service (using docker as well)
* [ ] work on app
