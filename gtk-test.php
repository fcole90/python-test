#!/usr/bin/php
<?php
 
function pressed()
{
    echo "Hello again - The button was pressed!\n";
}
 
$window = new GtkWindow();
$button = new GtkButton('Click Me');
 
$window->set_title('Hello World!');
$window->connect_simple('destroy', array('Gtk', 'main_quit'));
$button->connect_simple('clicked', 'pressed');
 
$window->add($button);
$window->show_all();
 
Gtk::main();
 
?>

