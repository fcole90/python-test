#!/usr/bin/php
<?php

class name {

	
	function say(){
	echo "\n";
    echo "Grazie, continuiamo...\n";
	echo "Come ti chiami?\n";
	$name = fgets(STDIN);
	echo "Ci vedremo presto ", $name, "           ______
          |======|
         |========|  	 _____________
         ///\\\\\\\\\\\\\    /               \
          |/o\ /o\ |  | MUAHAHAAHAHAHA! |
         /  /oo\    \  \ ______________/
         |  _____   |  |/
      ___ \ \___/  /___
     /     \______/      \\ \\n";
     	}
}

echo "Sei sicuro di volere continuare?\n";
$line = fgets(STDIN);

if(trim($line) == 'si'){
    	 
    	$name = new Name;
    	$name->say();
    }
else if(trim($line) == 's'){    
    
    	$name = new Name;
    	$name->say();
    
    }

else {
echo "KABOOOOOOOOOOOOOOOOOOM!\n";
    exit;
    }
?>
