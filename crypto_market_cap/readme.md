# CoinMarketCap API Integration with uAgents Hackathon Project

## Introduction

Welcome to our Hackathon project where we integrate the CoinMarketCap API with Fetch.ai AI Agent technology to create innovative solutions in the world of cryptocurrencies. In this project, we aim to provide real-time data on cryptocurrencies, fetch relevant news, and discover the top trending cryptocurrencies using uAgents.

![Project Image](insert_image_link_here)

## Problem Statement

Our challenge was to integrate the CoinMarketCap API with Fetch.ai AI Agent technology to solve a problem or create something innovative and provide a business useCase of it . We aimed to go beyond simple integration and present creative use cases for this combination of technologies.

## CoinMarketCap API

The CoinMarketCap API is a Text2Text integration that provides comprehensive data on cryptocurrencies. You can learn more about it [here](https://rapidapi.com/zakutynsky/api/CoinMarketCap/).

## User Input

To use our agents, you need to enter a cryptocurrency symbol as input on DeltaV. The symbol should be a valid cryptocurrency symbol like `ETH` for Ethereum, `BTC` for Bitcoin, `XRP` for Ripple, `SOL` for Solana, etc.

Here's an example of how to enter an input:

1. Open DeltaV.
2. Select the agent you want to use (CryptoDataAgent, CryptoNewsAgent, or TrendingCryptoAgent).
3. In the input field, enter the cryptocurrency symbol. For example, if you want data on Ethereum, enter `ETH`.
4. Click on the 'Send' button.

![Input](./src/images/input.jpg)



The agent will then fetch and display the data related to the cryptocurrency symbol you entered.

## uAgents Integration

We integrated the CoinMarketCap API with uAgents to create two agents:

1. **CryptoDataAgent**: Provides real-time data on the requested cryptocurrency.

| Name     | Symbol | Price            | Volume (24h)       | Change (24h) | Market Cap           |
|----------|--------|------------------|---------------------|--------------|----------------------|
| Bitcoin  | BTC    | 66863.51170428682| 43620642781.30312   | -4.76221334% | 1315925261517.3535   |
| Ethereum | ETH    | 3210.858383837866| 21614062100.60566   | -8.52252725% | 385530857439.1761    |

![Crypto_data_Output](./src/images/crypto_data.jpg)

2. **CryptoNewsAgent**: Fetches relevant news articles related to the requested cryptocurrency.


3. **TrendingCryptoAgent**: Identifies the top trending cryptocurrencies globally.

![Crypto_News_Output](./src/images/news.jpg)


## Video Demo

[![News and Crypto_data](./src/videos/WhatsApp%20Video%202024-04-13%20at%2007.50.54_a3fb4d172323.mp4)]


[![Crypto_data and Recommendation](./src/videos/WhatsApp%20Video%202024-04-13%20at%2007.51.04_9fc3e341.mp4)]

