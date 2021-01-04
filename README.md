<p>
	This is an open source robot interacting with Streamlab's soket api to 
	trigger event on specific alert types such as
	donations, subscription, etc.
</p>

#Hardware 
<p>
	The software is made in Python wich make easy to modify and port to other device type
	but the current configuration, installatiion setup and the easy installaion setup has been 
	designed for a raspberry pi reunning a debian base linux distribution such as 
	[raspbian](https://www.raspbian.org/). A 3.3 volt output is emited to pin 7 (GPIO) (this can be changed if you
	modify the source code)
</p>

#Installation

###Easy Install
<p>
	If you have a debian base operating systeme you can execute the easyInstal it will install every dipendencies using
	pip3 and apt-get. This install is recommended for users not familiar with linux.
</p>

```
$./easyInstall
```

###Install
<p>
	If you are familiar with linux and or alreay have python3 and pip3 installed you can simply execute the 
	install file wich will install every python dependencies required
</p>

```
$./install
```

###Configurin Socket API Token
<p>
	To interact with streamlabs, the bot will the 
	[socket API token](https://streamlabs.com/dashboard#/settings/api-settings) 
	wich allows you to identefy yourself to streamlabs.
	You can copy paste you token in /usr/lib/slp in the indicaded space
</p>


#Starting the bot
<p>
	To start the bot simply type the command slp. If you want to stop it, Simply press Ctrl + c.
</p>

```
$slp
preparing bot
clean up
...
```

#Configuration
<p>
	You can configure wich event triggers the bot and what amount (when it comes to bits and donations).
	Keep in mind that the donation is not put to scale with a specific curency which means
	5$ and 5€ will be worth the same (5). The config file /etc/slpConfig.json is an array of object (rules)
	which looks like this.
</p>

```
{
	"name": "donation",
	"value": 70,
	"on": true
}
```

<p>
	The "name" property is map to the actual type property sent by streamlabs wich means you if a new alert types ever
	gets released you could add it in with out chanching the code. This also means you should not change the name of the
	rules or the bot will not recognise it. The "value" property represents the threashold at witch the bot gets
	triggered. In this example above, 70 is the minimum amount of for the bot to get triggers when it comes to
	donations. The property "on" simply indicates to the bot if the rule is active, false the bot will ignore the rule,
	true the bot will use the rule. Keep in mind that every time you change a rule (the config file), 
	you must restart the bot.
</p>
