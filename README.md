# astroplot

The purpose of the Astroplot project is democratizing investment activities from selected few to people like us who do not have deep financial knowledge. We believe that the latest machine learning techniques can help us to optimize our investment decisions.

# brand

![astroplot-logo](/web/static/img/astroplot-logo.png "logo")

# algorithm

Currently, our price prediction using four machine learning models include the followings:

- CNN
In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks, most commonly applied to analyzing visual imagery.

- LSTM
Long short-term memory (LSTM) units (or blocks) are a building unit for layers of a recurrent neural network (RNN). A RNN composed of LSTM units is often called an LSTM network.

- custom MLRP
A multilayer perceptron (MLP) is a feedforward artificial neural network model that maps sets of input data onto a set of appropriate outputs.

- KNeighborsRegressor
The k-nearest neighbors (KNN) algorithm is a non-parametric algorithm that can be used for either classification or regression.

# contributors
Without dedicated contributions from communities, we are not able to come this far. Thank you for generous support to make this happen. PRs and bug reports are welcome, and we are actively opening up the Astroplot roadmap to facilitate for external contributors.  

- [kaeken](https://github.com/kaeken1jp)

- [Peter Mears](https://github.com/mrhappymac)

**How to contribute**
1. install virtualenv in the local computer
2. clone the latest git project
3. git log (if this doesn't work then)
    a. git fetch --all
    b. git reset --hard origin/master
4. pip3 install -r requirements.txt
5. python manage.py migrate
6. python manage.py runserver

# reference
Special thanks to the articles that let us explore the frontiers of using machine learning to predict the cryptocurrency prices:

- [Predicting Cryptocurrency Price With Tensorflow and Keras](https://medium.com/@huangkh19951228/predicting-cryptocurrency-price-with-tensorflow-and-keras-e1674b0dc58a)

- [Bitcoin price forecasting with deep learning algorithms](https://medium.com/activewizards-machine-learning-company/bitcoin-price-forecasting-with-deep-learning-algorithms-eb578a2387a3)

- [A Deep Learning Approach to Predicting Cryptocurrency Prices](https://github.com/llSourcell/ethereum_future/blob/master/A%20Deep%20Learning%20Approach%20to%20Predicting%20Cryptocurrency%20Prices.ipynb)
