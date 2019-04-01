#!/usr/bin/python3
from sys import argv
from webhook import Webhook,RequestTypes
import json

CONTROL_FILE = "controls.json"

def ReadJSONFile(strFileName):
	try:
		with open(strFileName,"r") as f:
			return json.loads(f.read())
	except:
		return None

def GetCommandObject(command,controlCommands):
	for cur in controlCommands:
		cmdObj = cur.get("commandId",None)
		if not cmdObj:
			continue
		if cmdObj != command:
			continue
		cur["requestType"] = cur.get("requestType","POST")
		cur["data"] = cur.get("data","")
		return cur


if __name__ == "__main__":
	if len(argv) < 2:
		print("You must pass in a command")
		exit()
	controlCommands = ReadJSONFile(CONTROL_FILE)
	if not controlCommands:
		print("Failed to load {}".format(CONTROL_FILE))
		exit()
	command = argv[1].lower()
	dictCommand = GetCommandObject(command,controlCommands.get("commands",{}))
	if not dictCommand:
		print("Not a valid command")
		exit()
	rType = RequestTypes.POST if dictCommand["requestType"].upper() == "POST" else RequestTypes.GET
	currentWebhook = Webhook(dictCommand["hookUrl"],dictCommand["data"].encode(),rType)
	if not currentWebhook.Trigger():
		print("There was an issue triggering the webhook")