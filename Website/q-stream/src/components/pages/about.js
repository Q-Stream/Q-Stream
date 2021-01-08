import React from 'react';
import { Jumbotron, Container, Breadcrumb } from 'react-bootstrap';
import './about.css'

function About() {
    return(
        <div className="about">
            <Jumbotron fluid className="jumbo-abt">
                <Container fluid className="cont-abt">
                    <Breadcrumb>
                        <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                        <Breadcrumb.Item active>About Us</Breadcrumb.Item>
                    </Breadcrumb>
                    <h1>About Us</h1>
                    <h3>Q-Stream is a free, open-source online media player that has a slew of great features. It supports various media platforms such as Youtube, Twitch, etc.</h3>
                    <h2>Contributions</h2>
                    <h3>As mentioned, being an Open Source Software, the Q-Stream Media Player is open to any contributions. Head over to our <a href="https://github.com/Swastik1710/Q-Stream">Github Repo</a> to get started.</h3>
                </Container>
            </Jumbotron>
        </div>
    )
}

export default About;