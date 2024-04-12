# from pydantic import BaseModel

class CryptoRequest(BaseModel):
    symbols: str

crypto_protocol = Protocol("Crypto")

@crypto_protocol.on_message(model=CryptoRequest, replies=UAgentResponse)
async def get_crypto_data(ctx: Context, sender: str, msg: CryptoRequest):
    """Fetch cryptocurrency data from CoinMarketCap API."""
    symbols = msg.symbols.replace(" ", "").upper()
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbols}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '75614851-5627-47c1-8b58-3ed65688deae',  # replace 'your_api_key' with your actual API key
    }
    try:
        ctx.logger.info(f"Attempting to fetch data for {msg.symbols}")
        crypto_data = requests.get(url, headers=headers)
        crypto_data.raise_for_status()
        data = crypto_data.json()

        # Extract specific fields from the JSON response and format them as a string
        text_data = ""
        for symbol, crypto in data['data'].items():
            name = crypto['name']
            price = crypto['quote']['USD']['price']
            volume_24h = crypto['quote']['USD']['volume_24h']
            percent_change_24h = crypto['quote']['USD']['percent_change_24h']
            market_cap = crypto['quote']['USD']['market_cap']

            text_data += f"Name: {name}, Symbol: {symbol}, Price: {price}, Volume (24h): {volume_24h}, Change (24h): {percent_change_24h}%, Market Cap: {market_cap}\n"

        ctx.logger.info(text_data)
        request_id = str(uuid.uuid4())
        await ctx.send(
            sender,
            UAgentResponse(
                message=text_data,
                type=UAgentResponseType.FINAL,
                request_id=request_id
            ),
        )
    except Exception as exc:
        ctx.logger.info(f"Error during Crypto Data retrieval: {exc}")
        return None

agent.include(crypto_protocol)