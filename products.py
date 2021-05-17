from flask_sqlalchemy import SQLAlchemy
from models import product 


from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://userid:password@localhost/database_name")
try:
    query="INSERT INTO  `product` (`productid` ,`sku` ,`product_name` ,`description`, 'image, quantity', 'regular_price', 'discount_price', 'product_rating', 'product_review')  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    my_data=[('1', '456789', 'ChuckIt Ultra Ball', 'ULTRA BOUNCE BALL: This ball toy for dogs entices play withhigh impact bouncing! Play fetch at the lake or pool thanks to the lightweight, buoyant design. Compatible with Chuckit! ball launcher.' , '/templates/assets/product_img/ChuckIt Ultra Ball.jpg', '10', '100')
        
    my_data=[('2', '813578', 'Up Country Mustache Dog Leash ', ' The ultimate accessory for every hipster dog! Hand sewn with attention to detail. Beautiful and durable. Brass Hardware. Matching Leash Sold . Separately ' , '/templates/assets/product_img/hipster_collar.jpg', '20', '100')    
    
    my_data=[('3', '541248', 'Alfie Pet - Chico Reversible Pet Sling Carrier ', 'CLOSE TO HEART: Our sling bag allows you to keep your dog close to your body where you can touch, hug, and talk to them ' , '/templates/assets/product_img/dog_messanger_bag.jpg', '50', '100')
    
    my_data=[('4', '15975', '', 'ULTRA BOUNCE BALL: This ball toy for dogs entices play withhigh impact bouncing! Play fetch at the lake or pool thanks to the lightweight, buoyant design. Compatible with Chuckit! ball launcher.' , '/templates/assets/product_img/ChuckIt Ultra Ball.jpg', '10', '100')

    my_data=[('5', '185746', 'Walkee Paws Snug Fit Dog Leggings', 'ULTRA BOUNCE BALL: This ball toy for dogs entices play withhigh impact bouncing! Play fetch at the lake or pool thanks to the lightweight, buoyant design. Compatible with Chuckit! ball launcher.' , '/templates/assets/product_img/dog_leggings.jpg', '10', '100')

    my_data=[('6', '456789', 'Hello Kitty Cat Backpack Space Capsule', 'Durable & Spacious, Right Backpack Size-the porous mesh is breathable, so that your pet is more airy and breathable inside .Made from pc and Oxford fabric.Measured probably 14L X10.6WX15.7H ,Load-bearing up to about 13.2lbs ' , '/templates/assets/product_img/cat space backback.jpg', '75', '25')

    my_data=[('7', '812578', 'Dancing Fish Toy', 'THE CAT’S MEOW – Make play fin-tastic with AmazinglyCat’s dancing fish kitty toy! Your catnip-filled toy fish flaps to life once playtime begins, beckoning every bat, bite, chew, and chase! ' , '/templates/assets/product_img/dancing fish.jpg', '40', '1000')

        ]
    