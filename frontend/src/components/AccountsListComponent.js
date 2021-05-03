import React from "react";

function AccountsList(props) {
    const accounts = fetch("eduspace/accounts")
    .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });

    const list = accounts.map((contact) => {
        return (
            <li key={contact.id}>
                {contact.name} - {contact.emdail}
            </li>
        )
    })

    return (
        <div>
            <ul>
                {list}
            </ul>
        </div>
    )
}

export default AccountsList;
