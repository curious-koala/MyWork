from flask import Flask
from flask import request


app = Flask(__name__)
# Creating the homepage which shows the list of all the selective words.
@app.route('/', methods = ['GET'])
def word_list():
    #return "Welcome! word_list= []. Plese enter the words is required to be found and replaced in output here. Use the format: url/word?input=xyz abc. For output please use: url/request/input?xyz xyz."
    word_list = ['Google', 'Microsoft', 'Amazon', 'Oracle', 'Deloitte']
    #word_input = str(request.args.get('input')) #/word?Google+,+Amazon+,+Oracle...
    #word_list.append(word_input)
    
    return word_list


# Creating the request page which will work on word find and replacement
@app.route('/request/', methods = ['GET'])
def request_page():
    words_list = word_list()
    user_query = request.args.get('input') # request/?input=Hello_Google
    
    for key in words_list:
        if key in user_query:
            user_query= user_query.replace (key, key + u'\N{COPYRIGHT SIGN}') #\xa9
    
    return user_query

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    