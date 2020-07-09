
name: 'Netease sign in'

on:
  push:
    branches: 
      - master
  schedule:
    - cron: '0 5 * * *'

jobs:
  netease:
    runs-on: ubuntu-latest
    steps:
    - name: 'Checkout codes'
      uses: actions/checkout@v2
    - name: 'Set python'
      uses: actions/setup-python@v1
      with:
        python-version: '3.x'
    - name: 'Install dependencies'
      run: python -m pip install --upgrade DecryptLogin
    - name: 'signin'
      env:
        NETEASE_USERNAME: ${{ secrets.NETEASE_USERNAME }}
        NETEASE_PASSWORD: ${{ secrets.NETEASE_PASSWORD }}
      run: python signin.py
