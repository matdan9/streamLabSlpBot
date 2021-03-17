<p>
	This is an open source robot interacting with Streamlab's soket api to 
	trigger events on specific alert types such as
	donations, subscription, etc.
</p>

<h1>Hardware</h1> 
<p>
	The software is made in Python which makes it easy to modify and port to other device types,
	but the current "configuration", "installation setup" and "the easy installaion setup" has been 
	designed for a raspberry pi running a debian base linux distribution such as 
	<a href="https://www.raspbian.org/">raspbian</a>. A 3.3 volt output is emited to pin 7 (GPIO) (this can be changed only if you
	modify the source code for now)
</p>

<h1> Installation </h1>

<h3> Easy Install </h3>
<p>
	If you have a debian base operating system you can execute the easyInstall.sh file. 
	It will install every dipendencies using
	pip3 and apt-get. This install is recommended for users not familiar with linux.
</p>

```
$./easyInstall.sh
```

<h3> Install </h3>
<p>
	If you are familiar with linux and or alreay have python3 and 
	pip3 installed you can simply execute the 
	install.sh file which will install every python dependencies required.
</p>

```
$./install.sh
```

<h3> Configuring the Socket API Token </h3>
<p>
	To interact with streamlabs, the bot will use the 
	<a href="https://streamlabs.com/dashboard#/settings/api-settings">socket API token</a> 
	which allows you to identefy yourself to streamlabs.
	You can copy paste you token in /usr/lib/slp in the indicaded space.
	Keep in mind that will be saved in plane text.
</p>


<h1> Starting the bot </h1>
<p>
	To start the bot simply type the command slp. If you want to stop it, Simply press Ctrl + c.
</p>

```
$slp
preparing bot
clean up
...
```

<h1> Configuration </h1>
<p>
	You can configure which event triggers the bot and at what amount (when it comes to bits and donations).
	Keep in mind that the donation is not put to scale with a specific curency which means
	5$ and 5€ will be worth the same amount (5). The config file /etc/slpConfig.json is an array of object (rules)
	which look like this.
</p>

```
{
	"name": "donation",
	"value": 70,
	"on": true
}
```

<p>
	The "name" property is map to the actual type property sent by streamlabs 
	which means you if a new alert type ever gets released you could add it 
	in without chanching the code. This also means you should not change the name of the
	rules or the bot will not recognise them. 
</p>
<p>
	The "value" property represents the 
	threashold at which the bot gets triggered. In this example, 70 is the minimum 
	amount of for the bot to get triggered, when it comes to donations. 
</p>
<p>
	The property "on" simply 
	indicates to the bot if the rule is active, ```false``` the bot will ignore the rule,
	```true``` the bot will use the rule. Keep in mind that every time you change a rule (the config file), 
	you must restart the bot.
</p>
