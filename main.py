from flask import Flask, render_template, request
import requests


BASE_URL = 'https://www.gamerpower.com/api/'

app = Flask(__name__)

def get_giveaways(platform=None, type=None, sort_by=None):
    url = f"{BASE_URL}giveaways"
    params = {}
    if platform:
        params['platform'] = platform
    if type:
        params['type'] = type
    if sort_by:
        params['sort-by'] = sort_by
 
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


@app.route('/')
def index():
    platform = request.args.get('platform')
    types = request.args.get('type')
    sort_by = request.args.get('sort-by')
    giveaways = get_giveaways(platform=platform, type=types, sort_by=sort_by)
    return render_template('index.html', giveaways=giveaways)
if __name__ == '__main__':
    app.run(debug=True)