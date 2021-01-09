import React from 'react';
import { Jumbotron, Container, Breadcrumb } from 'react-bootstrap';
import './downloads.css';

function Downloads() {
    return(
        <div className="download">
            <Jumbotron fluid className="jumbo-dnld">
                <Container fluid>
                    <Breadcrumb>
                        <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                        <Breadcrumb.Item active>Downloads</Breadcrumb.Item>
                    </Breadcrumb>
                    <h1>Downloads</h1>
                </Container>
            </Jumbotron>
        </div>
    )
}

export default Downloads;