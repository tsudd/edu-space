import React from 'react'
import { Link } from 'react-router-dom'
import {
  CardBody,
  CardTitle,
  Container,
  Card,
  CardSubtitle,
  Row,
  Button,
} from 'reactstrap'
import {
  API_MESSAGES,
  API_BASE_URL,
  ACCESS_TOKEN_NAME,
} from '../../constants/urls'
import { useAuth, useMessages } from '../../providers'

export const MessageList = () => {
  const { messages, setMessages } = useMessages()
  const { user, token } = useAuth()

  const handleDelete = async (id, e) => {
    e.preventDefault()
    try {
      const resp = await fetch(API_BASE_URL + API_MESSAGES + `/${id}`, {
        method: 'DELETE',
        headers: {
          Authorization: ACCESS_TOKEN_NAME + ' ' + token,
        },
      })
      if (resp.status == 204) {
        const newList = messages.filter((message) => message.id !== id)

        setMessages(newList)
        return
      }
    } catch (e) {
      console.error(e)
    }
  }
  return (
    <Container fluid="md">
      <Row>Messages</Row>
      {messages?.map((mes) => (
        <Card key={mes.id} md="5">
          <CardBody>
            {user && user.is_staff && (
              <Button
                id={mes.id}
                close
                onClick={(e) => handleDelete(mes.id, e)}
              />
            )}
            <CardTitle tag="h5">
              {mes.sender ? (
                <div>
                  Message from {mes.sender.user.name} {mes.sender.user.surname}.
                </div>
              ) : (
                <div>Message</div>
              )}
            </CardTitle>
            <CardSubtitle tag="h6" className="mb-2 text-muted">
              {mes.creation_datetime}
            </CardSubtitle>
            {mes.text}
          </CardBody>
        </Card>
      ))}
    </Container>
  )
}
