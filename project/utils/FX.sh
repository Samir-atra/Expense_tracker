# get the access token
# curl -u FXAPI:z5l2KRWEXnmDvBhssPq7 \
#      -X POST https://auth-sandbox.abnamro.com/as/token.oauth2 \
#      -d 'grant_type=client_credentials&scope=fxtrade:allowedcurrencypairs:read fxtrade:settlementaccountgroups:read fxtrade:rates:read fxtrade:conversioncalculations:write fxtrade:quotes:read fxtrade:quotes:write fxtrade:orders:read fxtrade:orders:write'

# get the transfer rate from euro to US dollar
curl -X GET \
     https://api-sandbox.abnamro.com/v1/fxtrade/rates/EURUSD \
     -H "Accept: application/json" \
     -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkNrMXh1cHdGbXJ6X1A1eUJraDVNbW0yX1AzayIsInBpLmF0bSI6InU2ZDIifQ.eyJzY29wZSI6WyJmeHRyYWRlOmFsbG93ZWRjdXJyZW5jeXBhaXJzOnJlYWQiLCJmeHRyYWRlOnNldHRsZW1lbnRhY2NvdW50Z3JvdXBzOnJlYWQiLCJmeHRyYWRlOnJhdGVzOnJlYWQiLCJmeHRyYWRlOmNvbnZlcnNpb25jYWxjdWxhdGlvbnM6d3JpdGUiLCJmeHRyYWRlOnF1b3RlczpyZWFkIiwiZnh0cmFkZTpxdW90ZXM6d3JpdGUiLCJmeHRyYWRlOm9yZGVyczpyZWFkIiwiZnh0cmFkZTpvcmRlcnM6d3JpdGUiXSwiY2xpZW50X2lkIjoiRlhBUEkiLCJleHAiOjE2OTI5OTcyMjh9.Wz2J1lFlKyB4a99rVSnk9pc1AvkwdNkrVuY0fF3JVFZVrWXcfoPVuARbKybOEyTGt3nE27QI9Usrc-LSkmIB65btQ2UvNXqcxvQBit3nXVdGR63tKY2jml4xj9jRn6ntV9XESLzSj8-jAM-2TwK8qWjoOkDG2JrrntNCNIFmthuvdAgy66jtw29uHgYipVwpwn2dxRRSKPMbEsNXppXqbVV9R1IloBWvq_T_g3qUhxnJLVW24FK1vR4LBlgoh5r9vcOCRmwOm1TlgDxqN8FyUaQRx6vrcxTlHe7OHlOL7ME7CmcJv9nSBqxC-LpJhAf5E625ypDk46Bdu8Ya0-_PzQ" \
     -H "API-Key: {API Key}"