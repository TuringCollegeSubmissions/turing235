This repository contains basic API created with Flask, containing
linear regression model on house prices.
Available endpoints are: ("/") and ("/predict"). First one displays project number,
"/predict" accepts input X_test data in json format and returns predicted house price.

For example, if you do a POST request with data in the following format:
```
{
    "input": [
  [1.8337e-01, 0.0000e+00, 2.7740e+01, 0.0000e+00, 6.0900e-01, 5.4140e+00,
  9.8300e+01, 1.7554e+00, 4.0000e+00, 7.1100e+02, 2.0100e+01, 3.4405e+02,
  2.3970e+01]
  ]
}
```
you would receive a response similar to this: 
```
{"Predicted values": [8.066137161274241]}
```

Hosted address: https://carlitto.herokuapp.com/