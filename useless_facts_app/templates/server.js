const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

app.get("/get-fact", (req, res) => {
    res.json({ fact: "Octopuses have three hearts!" });
});

app.get("/get-meme", (req, res) => {
    res.json({
        title: "Funny Meme",
        url: "https://i.imgur.com/J2x7Lvh.jpeg",
        postLink: "https://reddit.com",
    });
});

app.listen(3000, () => console.log("Server running on port 3000"));
