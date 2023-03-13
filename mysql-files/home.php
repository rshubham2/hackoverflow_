<?php 
session_start();

if (isset($_SESSION['id']) && isset($_SESSION['user_name'])) {

 ?>
<!DOCTYPE html>
<html>
<head>
	<title>rent'z</title>
	
</head>
<body>
<style>
     body {
	background: #23242a;
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
	flex-direction: column;
}
h1
{
color: #45f3ff;
font-weight: 525;
text-align: center;
letter-spacing: 0.1em;
}
.links
{
display: flex;
justify-content: space-between;
color: grey;
}
.links a
{
margin: 10px 0;
font-size: 0.75em;
color: #8f8f8f;
text-decoration: beige;
}
.links a:hover,
.links a:nth-child(2)
{
color: #45f3ff;
}
</style>

     <h1>Hello, <?php echo $_SESSION['name']; ?></h1>
     <div class="links">
     <h2><a href="http://127.0.0.1:8000/index.html">Continue Shopping</a></h2></div>
</body>
</html>

<?php 
}else{
     header("Location: index.php");
     exit();
}
 ?>