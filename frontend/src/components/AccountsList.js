import React, { useState, useEffect } from 'react'

export const AccountsList = () => {
  const [accounts, setAccounts] = useState()

  useEffect(() => {
    const getAccounts = async () => {
      const response = await fetch('api/accounts')
      setAccounts((await response.json()).results)
    }
    void getAccounts()
  }, [setAccounts])

  return (
    <div>
      {accounts && (
        <ul>
          {accounts.map(({ id, name, email }) => (
            <li key={id}>
              {name} - {email}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default AccountsList
