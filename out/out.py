from out.slack import SlackHook

def out(config=None, results=""):
    if config == None:
        print(results)
        return

    slack_hook = config['slack_hook']

    if len(config["slack_hook"]) > 0:
        slack = SlackHook(slack_hook)
        slack.send(results)
        return

    print(results)
