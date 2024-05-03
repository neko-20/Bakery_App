from flask import Flask, render_template
import pandas as pd
import ast

df_csv = pd.read_csv(" ") # 特徴単語のディレクトリ指定
df_csv['no'] = df_csv['id'].str.replace('ID-','')
df_csv['text1'] = [ast.literal_eval(d) for d in df_csv['text_top20']]
df_csv['text2'] = [ast.literal_eval(d) for d in df_csv['tfidf_top20']]

app = Flask(__name__, static_folder='./public/static', template_folder='./public')

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/data')
def get_data():
    df = df_csv[['no', 'store_name', 'score', 'review_cnt', 'text1', 'text2']]
    return df.to_json(orient='records', force_ascii=False)

if __name__=='__main__':
    app.run(debug=True)
