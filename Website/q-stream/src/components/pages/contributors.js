import React from 'react';
import { Jumbotron, Container, Breadcrumb } from 'react-bootstrap';
import './contributors.css';

function Contributors() {
    return (
        <div className="contri">
            <Jumbotron fluid className="jumbo">
                <Container fluid className="cont">
                    <Breadcrumb>
                        <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                        <Breadcrumb.Item active>Contributors</Breadcrumb.Item>
                    </Breadcrumb>
                    <h1>Contributors</h1>
                    <a href="https://github.com/Q-Stream/Q-Stream/graphs/contributors">
                        <img src="https://contrib.rocks/image?repo=Q-Stream/Q-Stream" />
                    </a>
                </Container>
            </Jumbotron>
        </div>
    )
}

export default Contributors;