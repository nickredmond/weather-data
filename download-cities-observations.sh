echo "downloading observations for "$2

response=$(curl $1/observations)
echo $response >> observations/observations-$2.json