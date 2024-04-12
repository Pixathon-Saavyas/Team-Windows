# CoinMarketCap API Integration with uAgents Hackathon Project

## Introduction

Welcome to our Hackathon project where we integrate the CoinMarketCap API with Fetch.ai AI Agent technology to create innovative solutions in the world of cryptocurrencies. In this project, we aim to provide real-time data on cryptocurrencies, fetch relevant news, and discover the top trending cryptocurrencies using uAgents.

![Project Image](insert_image_link_here)

## Problem Statement

Our challenge was to integrate the CoinMarketCap API with Fetch.ai AI Agent technology to solve a problem or create something innovative and provide a business useCase of it . We aimed to go beyond simple integration and present creative use cases for this combination of technologies.

## CoinMarketCap API

The CoinMarketCap API is a Text2Text integration that provides comprehensive data on cryptocurrencies. You can learn more about it [here](https://rapidapi.com/zakutynsky/api/CoinMarketCap/).

## uAgents Integration

We integrated the CoinMarketCap API with uAgents to create two agents:

1. **CryptoDataAgent**: Provides real-time data on the requested cryptocurrency.

| Name     | Symbol | Price            | Volume (24h)       | Change (24h) | Market Cap           |
|----------|--------|------------------|---------------------|--------------|----------------------|
| Bitcoin  | BTC    | 66863.51170428682| 43620642781.30312   | -4.76221334% | 1315925261517.3535   |
| Ethereum | ETH    | 3210.858383837866| 21614062100.60566   | -8.52252725% | 385530857439.1761    |

2. **CryptoNewsAgent**: Fetches relevant news articles related to the requested cryptocurrency.



and the thred agent is created using an external API of cryptoNews API
3. **TrendingCryptoAgent**: Identifies the top trending cryptocurrencies globally.

## Getting Started

To get started with our project, follow these steps:

1. **Clone this repository.**
   ```bash
   git clone https://github.com/your_username/your_repository.git
