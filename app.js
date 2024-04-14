const dialogflow = require("dialogflow");
const uuid = require("uuid");
const body_parser = require("body-parser");
const express = require("express");
const app = express();
const sessionId = uuid.v4();

// PORT is being defined for my local machine
const port = 5000;
app.get("/", (req, res) => {
  res.send("HEllO WORLD");
});

// Middle wares for app
app.use( body_parser.urlencoded({
    extended: false,
  })
);
// ACCept request from any location / either from file protocol  or from any wehre else "*" for all
 app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");

  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );

  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-Requested-With,content-type"
  );

  res.setHeader("Access-Control-Allow-Credentials", true);

  // Pass to next layer of middleware
  next();
});

//route made as mentioned in the index.html
app.post("/send-msg", (req, res) => {
  runSample(req.body.MSG).then((data) => {
    res.send({ Reply: data });
  });
});

/**
 * Send a query to the dialogflow agent, and return the query result.
 * @param {string} projectId The project to be used
 */
async function runSample(msg, projectId = "samira-9yy9") {
  // Create a new session
  const sessionClient = new dialogflow.SessionsClient({
    keyFilename: "/home/sarthak/Desktop/SAM/samira-9yy9-02a64f2ccdad.json",
  }); // the key file is added

  const sessionPath = sessionClient.sessionPath(
    projectId,
    sessionId
  );


  // The text query request.
  const request = {
    session: sessionPath,
    queryInput: {
      text: {
        //  query to send to the dialogflow agent   ## msg is the user message entered by user
        text: msg,

        languageCode: "en-US",
      },
    },
  };

  // Sending request and logging result # messages to be presented in the console or in vscode
  const responses = await sessionClient.detectIntent(request);
  console.log("Detected intent");
  const result = responses[0].queryResult;
  console.log(`  Query: ${result.queryText}`);
  console.log(`  Response: ${result.fulfillmentText}`);
  if (result.intent) {
    console.log(`  Intent: ${result.intent.displayName}`);
  } else {
    console.log("  No intent matched.");
  }
  return result.fulfillmentText;
}

// local server to listening on port 5000

app.listen(port, () => {
  console.log("running on port " + port);
});
