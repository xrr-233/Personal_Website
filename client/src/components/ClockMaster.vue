<template>
  <div class="home_clock" ref="home_clock">
    <table class="table" ref="table">
      <thead>
        <tr>
          <th scope="col">&#009202;时钟</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td ref="table_clock">
            <main class="clock-display">
              <h1>Clock.js</h1>
              <div class="date-field">
                <div class="day-of-week">
                  <p class="day-alpha"></p>
                  <p class="placeholder_clock">mmmmmmmmm</p>
                  <p class="placeholder_clock">ooooooooo</p>
                  <p class="placeholder_clock">nnnnnnnnn</p>
                  <p class="placeholder_clock">ttttttttt</p>
                  <p class="placeholder_clock">uuuuuuuuu</p>
                  <p class="placeholder_clock">eeeeeeeee</p>
                  <p class="placeholder_clock">sssssssss</p>
                  <p class="placeholder_clock">wwwwwwwww</p>
                  <p class="placeholder_clock">hhhhhhhhh</p>
                  <p class="placeholder_clock">rrrrrrrrr</p>
                  <p class="placeholder_clock">fffffffff</p>
                  <p class="placeholder_clock">iiiiiiiii</p>
                  <p class="placeholder_clock">ddddddddd</p>
                  <p class="placeholder_clock">aaaaaaaaa</p>
                  <p class="placeholder_clock">yyyyyyyyy</p>
                </div>
                <div class="day-of-week-mobile">
                  <p class="day-alpha-mobile"></p>
                  <p class="placeholder_clock">mmm</p>
                  <p class="placeholder_clock">ooo</p>
                  <p class="placeholder_clock">nnn</p>
                  <p class="placeholder_clock">ttt</p>
                  <p class="placeholder_clock">uuu</p>
                  <p class="placeholder_clock">eee</p>
                  <p class="placeholder_clock">sss</p>
                  <p class="placeholder_clock">www</p>
                  <p class="placeholder_clock">hhh</p>
                  <p class="placeholder_clock">rrr</p>
                  <p class="placeholder_clock">fff</p>
                  <p class="placeholder_clock">iii</p>
                </div>
                <div class="month">
                  <p class="month-alpha"></p>
                  <p class="placeholder_clock">mmm</p>
                  <p class="placeholder_clock">ooo</p>
                  <p class="placeholder_clock">nnn</p>
                  <p class="placeholder_clock">ttt</p>
                  <p class="placeholder_clock">uuu</p>
                  <p class="placeholder_clock">eee</p>
                  <p class="placeholder_clock">sss</p>
                  <p class="placeholder_clock">www</p>
                  <p class="placeholder_clock">hhh</p>
                  <p class="placeholder_clock">rrr</p>
                  <p class="placeholder_clock">fff</p>
                  <p class="placeholder_clock">iii</p>
                  <p class="placeholder_clock">ddd</p>
                  <p class="placeholder_clock">aaa</p>
                  <p class="placeholder_clock">yyy</p>
                  <p class="type">month</p>
                </div>
                <div class="date">
                  <p class="date-number"></p>
                  <p class="placeholder_clock">88</p>
                  <p class="type">day</p>
                </div>
                <div class="year">
                  <p class="year-number"></p>
                  <p class="placeholder_clock">8888</p>
                  <p class="type">year</p>
                </div>
              </div>
              <div class="clock-field">
                <div class="numbers">
                  <p class="hours"></p>
                  <p class="placeholder_clock">88</p>
                  <p class="type">hour</p>
                </div>
                <div class="colon">
                  <p>:</p>
                </div>
                <div class="numbers">
                  <p class="minutes"></p>
                  <p class="placeholder_clock">88</p>
                  <p class="type">minute</p>
                </div>
                <div class="colon">
                  <p>:</p>
                </div>
                <div class="numbers">
                  <p class="seconds"></p>
                  <p class="placeholder_clock">88</p>
                  <p class="type">second</p>
                </div>
                <div class="am-pm">
                  <div>
                    <p class="am">am</p>
                  </div>
                  <div>
                    <p class="pm">pm</p>
                  </div>
                </div>
              </div>
            </main>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import "../assets/css/font.css"

export default {
  name: "ClockMaster",
  methods: {
    getCurrentTime() {
      let fullDate = new Date()
      let month = fullDate.getMonth()
      let date = fullDate.getDate()
      let year = fullDate.getFullYear()
      let day = fullDate.getDay()
      let hours = fullDate.getHours()
      let minutes = fullDate.getMinutes()
      let seconds = fullDate.getSeconds()
      let period = (hours >= 12) ? "pm" : "am"

      window.clock = {}
      window.clock.time = {
        fullDate: fullDate,
        month: month,
        date: date,
        year: year,
        day: day,
        hours: hours,
        minutes: minutes,
        seconds: seconds,
        period: period
      }
    },

    displayCurrentTime() {
      let day = window.clock.time.day
      let month = window.clock.time.month
      let date = window.clock.time.date
      let year = window.clock.time.year
      let hours = window.clock.time.hours
      let minutes = window.clock.time.minutes
      let seconds = window.clock.time.seconds
      let period = window.clock.time.period

      //formats hours
      hours = (hours > 12) ? (hours - 12) : hours
      hours = (hours === 0) ? 12 : hours
      hours = (hours <= 9) ? ("0" + hours) : hours
      //formats minutes
      minutes = (minutes <= 9) ? ("0" + minutes) : minutes
      //formats seconds
      seconds = (seconds <= 9) ? ("0" + seconds) : seconds
      //formats day
      let days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
      let dayText = ``
      if (days[day].length === 6) dayText = `<span style="color: #2b2828;">ooo</span>${days[day]}`
      if (days[day].length === 7) dayText = `<span style="color: #2b2828;">oo</span>${days[day]}`
      if (days[day].length === 8) dayText = `<span style="color: #2b2828;">o</span>${days[day]}`
      if (days[day].length === 9) dayText = `<span style="color: #2b2828;"></span>${days[day]}`
      //formats mobile day
      let mobileDays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
      //formats month
      let months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
      //formats date
      date = (date <= 9) ? ("0" + date) : date

      // targets the html
      const dayHtml = document.getElementsByClassName('day-alpha')[0]
      const mobileDayHtml = document.getElementsByClassName('day-alpha-mobile')[0]
      const monthHtml = document.getElementsByClassName('month-alpha')[0]
      const dateHtml = document.getElementsByClassName('date-number')[0]
      const yearHtml = document.getElementsByClassName('year-number')[0]
      const hoursHtml = document.getElementsByClassName('hours')[0]
      const minutesHtml = document.getElementsByClassName('minutes')[0]
      const secondsHtml = document.getElementsByClassName('seconds')[0]
      const periodHtml = document.getElementsByClassName(period)[0]

      // changes the html values
      dayHtml.innerHTML = dayText
      mobileDayHtml.innerHTML = mobileDays[day]
      monthHtml.innerHTML = months[month]
      dateHtml.innerHTML = date
      yearHtml.innerHTML = year
      hoursHtml.innerHTML = hours
      minutesHtml.innerHTML = minutes
      secondsHtml.innerHTML = seconds
      periodHtml.classList.add("light-on")
    },

    resetClock() {
      const lights = document.querySelectorAll(".light-on")

      if (lights) {
        lights.forEach(item => {
          item.classList.remove("light-on")
        })
      }
    },

    /*updateClock() {
      resetClock()
      getCurrentTime()
      displayCurrentTime()
    },*/
  },
  activated() {
    this.resetClock()
    this.getCurrentTime()
    this.displayCurrentTime()
    this.timer = setInterval(() => {
      this.resetClock()
      this.getCurrentTime()
      this.displayCurrentTime()
    }, 1000)
  },
  deactivated() {
    clearInterval(this.timer)
  }
}
</script>

<style scoped>
* {
	margin: 0;
	padding: 0;
}
.home_clock {
	font-family: 'digital-7', sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
h1 {
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  font-family: sans-serif;
  padding-bottom: 15px;
}
main.clock-display {
  display: inline-block;
	text-align: center;
  padding: 15px 30px;
  border: solid 5px #ffffff;
  border-radius: 10px;
  background-color: #000000;
  color: #ffffff;
  box-shadow: 4px 4px 7px 4px rgba(0,0,0,.3);
  zoom: 60%
}
.light-on {
	color: #ffffff !important;
}

/* DATE */
.date-field {
	margin: 5px 0;
  display: flex;
  justify-content: space-between;
}
.date-field div {
	display: inline-block;
	position: relative;
}
.date-field div p {
	font-size: 34px;
	position: relative;
	z-index: 100;
}
.date-field div p.placeholder_clock {
	color: #2b2828;
	position: absolute;
	top: 0;
	z-index: 50;
}
.date-field div.day-of-week-mobile {
  display: none;
}
.date-field div.day-of-week p {
  font-size: 50px;
}
.date-field div p.type {
  font-size: 10px;
  font-weight: bold;
  font-family: sans-serif;
  text-transform: uppercase;
}
@media (max-width: 768px) {
  .date-field {
    justify-content: space-evenly;
  }
  .date-field div.day-of-week {
    display: none;
  }
  .date-field div.day-of-week-mobile {
    display: inline-block;
  }
  .date-field div.day-of-week-mobile p {
    font-size: 56px;
    margin-top: -2px;
  }
}
@media (max-width:550px) {
  .date-field div.day-of-week-mobile p {
    font-size: 50px;
    margin-top: 0;
  }
}
@media (max-width:468px) {
  .date-field div.day-of-week-mobile p {
    font-size: 42px;
  }
}
@media (max-width:400px) {
  .date-field div.day-of-week-mobile p {
    font-size: 20px;
  }
}

/* CLOCK */
.clock-field {
	margin: 5px 0;
  display: flex;
  justify-content: center;
}
.clock-field div {
	display: inline-block;
	position: relative;
}
.clock-field div p {
	font-size: 100px;
	position: relative;
	z-index: 100;
}
.clock-field .numbers .placeholder_clock {
	color: #2b2828;
	position: absolute;
	top: 0;
	z-index: 50;
}
.clock-field .numbers .type {
  font-size: 10px;
  font-weight: bold;
  font-family: sans-serif;
  text-transform: uppercase;
  margin-top: -10px;
}
.clock-field .am-pm {
	font-family: sans-serif;
	text-transform: uppercase;
	width: 20px;
}
.clock-field .am-pm div p {
	font-size: 12px;
	font-weight: bold;
	width: 100%;
}
.clock-field .am,
.clock-field .pm {
	color: #2b2828;
}

@media (max-width:768px) {
  main.clock-display {
    padding: 15px 30px;
  }
  .desktop-view {
    display: none;
  }
}

@media (max-width:550px) {
  .date-field div p {
    font-size: 30px;
  }
  .clock-field div p {
    font-size: 80px;
  }
}

@media (max-width:468px) {
  .date-field div p {
    font-size: 24px;
  }
  .clock-field div p {
    font-size: 60px;
  }
}

@media (max-width:400px) {
  .date-field div p {
    font-size: 20px;
  }
  .days .day p,
  .clock-field .am-pm div p {
    font-size: 10px;
  }
  .clock-field div p {
    font-size: 50px;
  }
}

@media (max-width:350px) {
  .date-field div p {
    font-size: 20px;
  }
  .clock-field div p {
    font-size: 43px;
  }
}

@media (max-width:320px) {
  .date-field div p {}
  .clock-field div p {
    font-size: 40px;
  }
}
</style>