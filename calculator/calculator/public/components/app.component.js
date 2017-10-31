Vue.component('sc-app', {
  template: `
    <b-container class="my-3">
      <b-row>
        <b-col md="6">
          <b-card header="Enter stock information"
                  bg-variant="dark" text-variant="white">
            <b-form @submit.prevent="getStockStats">
              <b-form-group label="Symbol">
                <b-form-input type="text" v-model="symbol" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Allotment">
                <b-form-input type="number" v-model="allotment" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Initial Share Price">
                <b-form-input type="number" v-model="initialSharePrice" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Final Share Price">
                <b-form-input type="number" v-model="finalSharePrice" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Sell Commission">
                <b-form-input type="number" v-model="sellCommission" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Buy Commission">
                <b-form-input type="number" v-model="buyCommission" required></b-form-input>
              </b-form-group>
              
              <b-form-group label="Capital Gain Tax Rate">
                <b-form-input type="number" v-model="capitalGainTaxRate" required></b-form-input>
              </b-form-group>
              
              <b-button v-b-toggle.stats type="submit" variant="info">Calculate</b-button>
            </b-form>
          </b-card>
        </b-col>
        
        <b-col md="6">
          <b-collapse id="stats">
            <b-card header="Statistics" header-bg-variant="info" header-text-variant="white">
              <dl class="row">
                <dt class="col-sm-9">Proceeds</dt>
                <dd class="col-sm-3">{{ stats.proceeds }}</dd>
                
                <dt class="col-sm-9">Cost</dt>
                <dd class="col-sm-3">{{ stats.cost }}</dd>
                
                <dt class="col-sm-9">Net Profit</dt>
                <dd class="col-sm-3">{{ stats.net_profit }}</dd>
                
                <dt class="col-sm-9">Return on Investment</dt>
                <dd class="col-sm-3">{{ stats.return_on_investment }}</dd>
                
                <dt class="col-sm-9">Break Even Price</dt>
                <dd class="col-sm-3">{{ stats.break_even_price }}</dd>
              </dl>
            </b-card>
          </b-collapse>
        </b-col>
      </b-row>
    </b-container>
  `,

  data: function() {
    return {
      symbol: null,
      allotment: null,
      initialSharePrice: null,
      finalSharePrice: null,
      sellCommission: null,
      buyCommission: null,
      capitalGainTaxRate: null,
      stats: {}
    }
  },

  methods: {
    getStockStats: function() {
      const self = this;
      const params = {
        symbol: this.symbol,
        allotment: this.allotment,
        initial_share_price: this.initialSharePrice,
        final_share_price: this.finalSharePrice,
        sell_commission: this.sellCommission,
        buy_commission: this.buyCommission,
        capital_gain_tax_rate: this.capitalGainTaxRate,
      };
      axios.get('/api/calculate', { params: params })
        .then(function(response) {
          self.stats = response.data;
        });
    }
  }
});
