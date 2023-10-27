# get the access token
AC=$(curl -u FXAPI:z5l2KRWEXnmDvBhssPq7 \
     -X POST https://auth-sandbox.abnamro.com/as/token.oauth2 \
     -d 'grant_type=client_credentials&scope=fxtrade:allowedcurrencypairs:read fxtrade:settlementaccountgroups:read fxtrade:rates:read fxtrade:conversioncalculations:write fxtrade:quotes:read fxtrade:quotes:write fxtrade:orders:read fxtrade:orders:write' | jq -r '.access_token')


# get the transfer rate from 1 to 2
curl -X GET \
     https://api-sandbox.abnamro.com/v1/fxtrade/rates/${1}${2} \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $AC" \
     -H "API-Key: API-KEY"


# 