 <!DOCTYPE html>
<html lang="en">
<head>
    <title>Output</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=devide-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
</head>

<body>
  <div class="container">
  <h2>Tags Symbol Table</h2>
             
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Tag Name</th>
        <th>Tag/Attribute</th>
        <th>Type</th>
        <th>Line number</th>
        <th>Status</th>
        <th>Comment</th>
      </tr>
    </thead>
    <tbody>
 <?php 
          //echo "hi";
      $file = $_POST['fileName'];
      //echo "hwllo";
      //echo $file;
          $arg = str_replace('"', '\"', $file);
          $python =  'C:\Program Files (x86)\Python';
          $path = 'test.py';
          //echo exec("$python $path", $output);
     
          passthru("python finalCode.py 1 \"$arg\"");
          //echo "after py";

          $myfile = fopen("op.txt", "r") or die("Unable to open file!");
      while(!feof($myfile)) {
        //echo fgets($myfile) . "<br>";
        $v = "";
        echo "<tr>";
        foreach (explode(" ",fgets($myfile)) as $v){
          if ($v == 'end') break;
          echo "<td>".$v."</td>";
        }

        echo "</tr>";
        if ($v == 'end') break;
      }
      
       echo " 
  
       </tbody>
      </table>
      <h2>Attribute Symbol Table</h2>
      <table class=\"table table-bordered\">
    <thead>
      <tr>
        <th>Attribute</th>
        <th>Tag/Attribute</th>
        <th>Value</th>
        <th>Tag</th>
      </tr>
    </thead>
    <tbody>";
      while(!feof($myfile)) {
        $i = 0;
        echo "<tr>";
        foreach (explode(" ",fgets($myfile)) as $v){
          if($i==4) break;
          echo "<td>".$v."</td>";
          $i++;
        }

        echo "</tr>";
        
      }
      fclose($myfile);
  ?>
</tbody>
</table>
</div>
 </body> 