# Kootabase system design 

    - This is design is a work in progress...

## Requirements clarification: 

    - Who are the users of this platform: 
      - crypto enthusiast who are willing to get started in crypto 
      - crypto veterans who are experienced with crypto currencies
      - professional traders 
      - institutional investors 
      - Crypto dealers

    - The platform allows traders (professional and amateurs) to trade crypto assets 
    - Users can make different types of orders (Market order, limit order, stop_loss_order etc..)
    - Users can open and close their positions
    - The platform allows traders to view the price of assets in real time 
    - Users can deposit fiat or crypto to currency into their account wallet for future trades 
    - users can receive their payments on external as well internal wallets
    - users can access the state of their transactions from the blockchain explorer
    - users can withdraw their deposits and profits
    - users can swap their currency with other listed on the platform


    # What about the admin? 
            - The admin can define roles for every users in the platform 
            - should be able to monitor key health metrics of the platform on a dashboard



    # Non functional requirements: 

            - The platform should be highly available 
            - The platform shouldbe 100% secure against theft and identify fraud 
            - The platform should be very regardant on money laundering practices
            - Attack proof
            - The transactions should be fast and secure
            - The users can access the platform from any device


## System API definition 

    - orderAsset(user_id, asset_name, amount, asset_price, order_type:[bid, ask]) 
    - depositFunds(user_id, wallet_id, currency_id) 
    - getWallet(user_id, wallet_address, currency_id) 
    - getPrice(user_id, market_id, ) 
    - getTransaction(user_id, transaction_id, market_id)



## Back of the envelope estimation 

        # numbers of transactions per/day: very few in the begining
        # how much time does it take to query a blockchain to verify wallet address and transactions
        # how much storage will we need? 
        # How many trades each user is allowed to make? 10 trades per day
        # What is the expected number of users? => 1 million in the first year


## Define the data model 

        => Models of intersets 

            - User 
              - user_id 
              - name 
              - password 
              - email 
              - phone_number 
           
            - Accounts
              - user_id 
              - balance
              - currency_id

            - Order: 
              - order_type 
              - market_id 
              - amount 
              - price 

## High level design 

            - Clients (Web, phone, tablet) 
            - Nginx gateway 
            - Monolith Backend 
            - Order routing (Task queue AMPQ, Redis) 
            - Mysql DB 
            - Docker container 
            - Kubernetes orchestrator 
            - Digital Ocean or GCP 

## Detailed Design 

        - Monolith backend (composed of many services) 
          - User accounts 
          - Transactions services 
          - Order matching engine 
          - Market data APIs 
          - Exchange rates API
          - Wallets 
          - Blockchain service

        => These servies can be grouped in  (Admin API, User API, Management API, EventAPI, TradingAPI, WebsocketAPI /)

## What are the potential bottlnecks: 

        - Liquidity shortage!!


