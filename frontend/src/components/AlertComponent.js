import React, { useState, useEffect } from 'react'
import { Alert } from 'reactstrap'

export const AlertComponent = (props) => {
  const [visible, setVisible] = useState(true)

  const onDismiss = () => {
    setVisible(false)
    props.hideError(null)
  }

  useEffect(() => {
    if (props.errorMessage !== null) {
      setVisible(true)
    } else {
      setVisible(false)
    }
  })

  return (
    <div className="col-md-6 m-auto">
      <Alert color="danger" isOpen={visible} toggle={onDismiss}>
        <div>
          <span>{props.errorMessage}</span>
        </div>
      </Alert>
    </div>
  )
}
