# py-cmd-trigger

## install
    npm install
    <or>
    npm i

## running
    npm start -- -t "API_TOKEN_HERE" -c "test" -cmd "invite" -i "@slackbot"

    <or>

    python index.py -t "API_TOKEN_HERE" -c "test" -cmd "invite" -i "@slackbot"

## options
* -t, --token => String - Your Slack API-token
* -cmd, --command => String - The slash command you want to use
* -c, --channel => String - The channel you want to post to
* -i, --instruction => String - all the text following your slash-command

## example
    python index.py -t "xyz" -c "test" -cmd "invite" -i "@slackbot"
