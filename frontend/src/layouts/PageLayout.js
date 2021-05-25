import React from 'react'
import { Col, Container, Row } from 'reactstrap'
import { Header, SubjectList } from './components'
import { MessageList } from './components/MessageList'

export const PageLayout = ({
  children,
  showSubjectList = true,
  showMessages = true,
}) => {
  return (
    <>
      <Header />
      <Container fluid={true}>
        <Row>
          {showSubjectList && (
            <Col md="3">
              <SubjectList />
            </Col>
          )}
          <Col>{children}</Col>
          {showMessages && (
            <Col md="3">
              <MessageList />
            </Col>
          )}
        </Row>
      </Container>
    </>
  )
}
