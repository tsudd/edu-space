import React, { useState, useEffect } from 'react'
import { Alert } from 'reactstrap'

export const AlertComponent = ({ visible, onDismiss, message }) => {
  return (
    <div className="col-md-6 m-auto">
      <Alert color="danger" isOpen={visible} toggle={onDismiss}>
        <div>
          <span>{message}</span>
        </div>
      </Alert>
    </div>
  )
}
