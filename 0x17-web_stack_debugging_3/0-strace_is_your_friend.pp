# This puppet script fixes the Word-Press site
exec { 'wp_fixer':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
