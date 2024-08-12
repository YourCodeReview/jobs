import { ref, set, onValue } from 'firebase/database'
import { database } from '@/firebase/firebase'

export const useDatabase = () => {
  const writeUserDataById = (userId, email, phone) => {
    set(ref(database, 'users/' + userId), {
      email,
      phone
    })
      .then(() => {
        console.log('Data written successfully!')
      })
      .catch((error) => {
        console.error('Error writing data:', error)
      })
  }

  const readUserDataById = (userId) => {
    return new Promise((resolve, reject) => {
      const userRef = ref(database, 'users/' + userId)
      onValue(userRef, (snapshot) => {
        const data = snapshot.val()
        if (data) {
          resolve(data)
        } else {
          reject('No data available for this user.')
        }
      })
    })
  }

  return { writeUserDataById, readUserDataById }
}
