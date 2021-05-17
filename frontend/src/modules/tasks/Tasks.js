import React, { useEffect, useState } from 'react'
import { useHistory, useParams } from 'react-router'
import {
  Container,
  Row,
  Card,
  CardText,
  CardSubtitle,
  CardBody,
  CardTitle,
  Col,
  Button,
} from 'reactstrap'
import { PageLayout } from '../../layouts'
import { useAuth } from '../../providers'
import {
  ACCESS_TOKEN_NAME,
  API_BASE_URL,
  API_SUBJECTS,
  API_TASKS,
  TASK_UPDATE_URL,
} from '../../constants/urls'

export const Tasks = () => {
  const { id } = useParams()
  const { token, user } = useAuth()
  const [tasks, setTasks] = useState(null)
  const [subject, setSubject] = useState(null)
  const history = useHistory()
  useEffect(() => {
    const getSubject = async () => {
      try {
        const resp = await fetch(API_BASE_URL + API_SUBJECTS + `/${id}`, {
          method: 'GET',
          headers: {
            Authorization: ACCESS_TOKEN_NAME + ' ' + token,
          },
        })
        if (resp.status == 204) {
          return
        }
        const json = await resp.json()
        if (resp.ok) {
          setTasks(json.tasks)
          setSubject(json.subject)
        }
      } catch (e) {
        console.error(e)
      }
    }
    void getSubject()
  }, [setTasks, setSubject, id, token])
  const handleDelete = async (id, e) => {
    e.preventDefault()
    try {
      const resp = await fetch(API_BASE_URL + API_TASKS + `/${id}`, {
        method: 'DELETE',
        headers: {
          Authorization: ACCESS_TOKEN_NAME + ' ' + token,
        },
      })
      if (resp.status == 204) {
        const newList = tasks.filter((task) => task.id !== id)

        setTasks(newList)
        return
      }
    } catch (e) {
      console.error(e)
    }
  }
  const handleUpdate = (task, e) => {
    e.preventDefault()
    history.push({
      pathname: TASK_UPDATE_URL,
      state: { task: { ...task, subject: id } },
    })
  }
  return (
    <PageLayout>
      {subject ? (
        <Container>
          <Row>
            <h2>{subject.name}</h2>
          </Row>
          <Row>
            <h5>{subject.description}</h5>
          </Row>
          <Row>
            <h3>{subject.name}</h3>
          </Row>
        </Container>
      ) : (
        <Container>
          <Row>
            <Col>
              <h2>No data...</h2>
            </Col>
          </Row>
        </Container>
      )}
      {tasks?.map((task) => (
        <Card key={task.id}>
          <CardBody>
            <CardTitle tag="h5">
              {task.name}
              {user && user.is_staff && (
                <div>
                  <Button
                    close
                    aria-label="Cancel"
                    onClick={(e) => handleUpdate(task, e)}
                  >
                    <span aria-hidden>&#9998;</span>
                  </Button>
                  <Button
                    id={task.id}
                    close
                    onClick={(e) => handleDelete(task.id, e)}
                  />
                </div>
              )}
            </CardTitle>

            <CardSubtitle tag="h6" className="mb-2 text-muted">
              Created {task.creation_date}
            </CardSubtitle>
            <CardText>{task.description}</CardText>
            {task.deadline != '' && (
              <Row>
                <CardSubtitle className="ml-auto">
                  Until {task.deadline}
                </CardSubtitle>
              </Row>
            )}
          </CardBody>
        </Card>
      ))}
    </PageLayout>
  )
}
